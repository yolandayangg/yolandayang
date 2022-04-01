infoDb=[]

infoDb.append({
    "firstName": "Yolanda",
    "lastName": "Yang",
    "DOB": "July 15",
    "residence": "San Diego",
    "email": "yolanda.sh2004@gmail.com",
    "apclassesTaken": ["AP Statistics", "AP CSP", "AP Calculus AB", "AP US History", "AP Biology"]
})
infoDb.append({
    "firstName": "John",
    "lastName": "Adams",
    "DOB": "July 18",
    "residence": "New York City",
    "email": "yolanda.sh2004@gmail.com",
    "apclassesTaken": ["AP Statistics", "AP CSP", "AP Calculus AB", "AP US History", "AP Biology"]
})
infoDb.append({
    "firstName": "John",
    "lastName": "Smith",
    "DOB": "July 16",
    "residence": "San Francisco",
    "email": "ilovecode@gmail.com",
    "apclassesTaken": ["AP Statistics", "AP CSP", "AP Calculus AB", "AP US History", "AP Biology"]
})
infoDb.append({
    "firstName": "George",
    "lastName": "Washington",
    "DOB": "July 17",
    "residence": "Washington DC",
    "email": "mrpresident@gmail.com",
    "apclassesTaken": ["AP Statistics", "AP CSP", "AP Calculus AB", "AP US History", "AP Biology"]
})
def print_data(n):
    print(infoDb[n]["firstName"], infoDb[n]["lastName"])
    print("\t", "AP classes taken: ", end="")
    print(", ".join(infoDb[n]["apclassesTaken"]))
    print()

def for_print_data():
    for i in range(len(infoDb)):
        print_data(i)

def while_print_data():
    x = 0
    while x < len(infoDb):
        print_data(x)
        x = x + 1

def recursive_print_data(n = 0):
    if n >= len(infoDb):
        return
    print_data(n)
    recursive_print_data(n + 1)