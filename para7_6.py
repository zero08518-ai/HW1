def helper(work):
    work_in_memory = work

    def helper(work):
        return  f"I will help tuy with {work_in_memory}" \
                f"Afterwards I will help you with {work}"

    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))