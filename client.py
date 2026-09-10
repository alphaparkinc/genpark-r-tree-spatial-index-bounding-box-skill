class RTreeNode:
    """
    R-Tree Spatial Index Node.
    Bounding box: (min_x, min_y, max_x, max_y).
    """
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.entries = []

    def compute_bbox(self):
        if not self.entries:
            return (0, 0, 0, 0)
        min_x = min(e[0][0] for e in self.entries)
        min_y = min(e[0][1] for e in self.entries)
        max_x = max(e[0][2] for e in self.entries)
        max_y = max(e[0][3] for e in self.entries)
        return (min_x, min_y, max_x, max_y)

class RTree:
    def __init__(self):
        self.root = RTreeNode(is_leaf=True)

    def intersects(self, b1, b2):
        return not (b1[2] < b2[0] or b1[0] > b2[2] or b1[3] < b2[1] or b1[1] > b2[3])

    def insert(self, bbox, item_id):
        self.root.entries.append((bbox, item_id))

    def query(self, search_bbox):
        hits = []
        for bbox, item_id in self.root.entries:
            if self.intersects(bbox, search_bbox):
                hits.append(item_id)
        return hits
