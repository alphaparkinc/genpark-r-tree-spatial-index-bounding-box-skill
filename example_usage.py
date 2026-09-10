from client import RTree

def main():
    print("=== Testing R-Tree Spatial Index ===")
    rt = RTree()
    rt.insert((0, 0, 10, 10), "building_A")
    rt.insert((20, 20, 30, 30), "building_B")

    query_box = (5, 5, 15, 15)
    hits = rt.query(query_box)
    print(f"Query {query_box} found: {hits}")

    assert hits == ["building_A"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
