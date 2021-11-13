def delete_keys(inputlist,inputdic):
    a = len(inputlist)
    for i in range(a):
        inputdic.pop(inputlist[i])
    return inputdic


dict = {"firstName": " Mohamed", "lastName":"Farag", "birthYear":1990, "nationality":"Egyptian"}
print(delete_keys(["lastName","birthYear"], dict))