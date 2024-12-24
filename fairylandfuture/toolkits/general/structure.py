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
    def build(cls, data: List[Dict[str, Any]], id_field: str = None, parent_id_field: str = None) -> List[Dict[str, Any]]:
        if not data:
            raise RuntimeError("Data is empty.")
        if not id_field:
            id_field = "id"
        if not parent_id_field:
            parent_id_field = "parent_id"

        nodes = dict()
        root_nodes = list()

        for item in data:
            node_id = item.get(id_field)
            parent_id = item.get(parent_id_field)
            node_data = item.copy()

            node = cls.node(id=node_id, parent_id=parent_id, data=node_data)
            nodes.update({node_id: node})

        for node in nodes.values():
            parent_id = node.get_parent_id()
            if parent_id is None or parent_id not in nodes:
                root_nodes.append(node)
            else:
                parent = nodes.get(parent_id)
                parent.add_child(node)

        return [node.to_dict() for node in root_nodes]
