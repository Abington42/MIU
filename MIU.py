
bucket = ["MI"]
def add_to_bucket(item, container):
    if item not in container:
        container.append(item)
        print(f"{item} added to bucket")

def rule1(item):
    if item[-1] == "I":
        new_item = item + "U"
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule2(item):
    if item[0] == "M":
        new_item = item + item[1:]
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule3(item):
    if item.find("III") != -1:
        new_item = item.replace("III", "U", 1)
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule4(item):
    if item.find("UU") != -1:
        new_item = item.remove("UU")
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def iterate_over(container):
    iterations = 0
    while "MU" not in container:
        for item in container:
            rule1(item)
            rule2(item)
            rule3(item)
            rule4(item)
            iterations += 1
        print(f"Iterations: {iterations}")
    print("MU")

iterate_over(bucket)

