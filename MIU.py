

bucket = ["MI"] #"MI" is given as an axiom
def add_to_bucket(item, container):
    if item not in container: #I only want new dirivations
        container.append(item)
        print(f"{item} added to bucket")

def rule1(item):#If the string ends in "I", you may add "U" to the end.
    """BUG: Infinite loop adding illegal string "IU" to bucket.
    it should not be possible to generate a string that doesn't
    start with "M", nor should it be possible to add redundant copies 
    of a particular string to the bucket.
    """
    if item[-1] == "I":
        new_item = item + "U"
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule2(item):# If you have Mx, you may dirive Mxx; all chars after "M" should be duplicated
        new_item = item + item[1:]
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule3(item):
    if item.find("III") != -1:# If the substring "III" appears in your string, you may replace it with "U"
        new_item = item.replace("III", "U", 1)#This should only replace the first occurrence per iteration
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def rule4(item):# If the substring "UU" appears in your string, you may delete it.
    if item.find("UU") != -1:
        new_item = item.remove("UU")#This should only remove the first occurrence per iteration
        add_to_bucket(new_item, bucket)
        print(f"{new_item} derived from {item}")

def iterate_over(container):
    """
    Starting with "MI",  recursively apply every applicable rule to each item in the 
    bucket, eventually producing every possible theorem that can be dirived from "MI".
    over successive iterations this should eventually produce "MU" or 
    keep looping forever if "MU" is not a theorem of the MIU system
    """
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

