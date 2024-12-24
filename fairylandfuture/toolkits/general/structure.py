# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-23 16:35:23 UTC+08:00
"""

from typing import Dict, Any, List

from fairylandfuture.core.superclass.structures import BaseStructureTreeNode


class TreeEntity:
    def build_tree(self, data: List[Dict[str, Any]], id_field: str, parent_id_field: str) -> List[Dict[str, Any]]:
        tree = []
        lookup = {item[id_field]: {**item, "children": []} for item in data}

        for item in data:
            parent_id = item.get(parent_id_field)
            node = lookup[item[id_field]]
            if parent_id is None:
                # 如果没有父节点，则为根节点
                tree.append(node)
            else:
                parent = lookup.get(parent_id)
                if parent:
                    parent["children"].append(node)
                else:
                    # 处理父节点不在数据中的情况
                    tree.append(node)
        return tree


class TreeBuilder:
    node = BaseStructureTreeNode

    @classmethod
    def build(cls, data: List[Dict[str, Any]], id_field: str = "id", parent_id_field: str = "parent_id") -> List[Dict[str, Any]]:
        if not data:
            raise ValueError("Input data cannot be empty.")

        nodes = {item.get(id_field): cls.node(item.get(id_field), parent_id=item.get(parent_id_field), data=item) for item in data}
        root_nodes = []

        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        return [node.to_dict() for node in root_nodes]


from typing import Dict, Any, List, Optional


class TreeBuilderV2:
    node = BaseStructureTreeNode

    @classmethod
    def build(
            cls,
            data: List[Dict[str, Any]],
            id_field: str = "id",
            parent_id_field: str = "parent_id",
            max_depth: Optional[int] = None  # 增加一个可选参数 max_depth
    ) -> List[Dict[str, Any]]:
        """
        构建树结构并返回限制在指定深度的树。

        :param data: 输入数据列表，每个字典表示一个节点。
        :param id_field: 表示 ID 的字段名称，默认值是 "id"。
        :param parent_id_field: 表示父 ID 的字段名称，默认值是 "parent_id"。
        :param max_depth: 限制返回树的最大深度，如果为 None 则返回完整树。
        :return: 按照层次构建的树数据列表。
        """
        if not data:
            raise ValueError("Input data cannot be empty.")

        # 创建所有节点
        nodes = {
            item.get(id_field): cls.node(
                item.get(id_field),
                parent_id=item.get(parent_id_field),
                data=item
            )
            for item in data
        }
        root_nodes = []

        # 构建树
        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        # 转换为字典，并按 max_depth 限制层数
        return [cls.limit_depth(node.to_dict(), max_depth) for node in root_nodes]

    @staticmethod
    def limit_depth(node: Dict[str, Any], max_depth: Optional[int], current_depth: int = 1) -> Dict[str, Any]:
        """
        限制树的深度，移除超过 max_depth 的子节点。

        :param node: 当前节点的字典表示。
        :param max_depth: 最大深度值，如果为 None 则不限制。
        :param current_depth: 当前节点的深度，从 1 开始。
        :return: 限制深度后的节点字典。
        """
        if max_depth is not None and current_depth >= max_depth:
            # 超过最大深度时移除子节点
            node.pop("children", None)
        else:
            # 否则递归处理子节点
            children = node.get("children", [])
            node["children"] = [
                TreeBuilder.limit_depth(child, max_depth, current_depth + 1)
                for child in children
            ]
        return node
