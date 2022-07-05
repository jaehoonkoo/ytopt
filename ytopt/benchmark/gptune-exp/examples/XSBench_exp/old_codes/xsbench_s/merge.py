import os

def merge_db(db_files_list):

    import json

    merged_json_data = {}

    merged_json_data["tuning_problem_name"] = "xsbench"
    merged_json_data["surrogate_model"] = []
    merged_json_data["func_eval"] = []

    nargs = len(db_files_list)

    print ("nargs: ", nargs)
    print ("db_files_list: ", db_files_list)

    for i in range(0, nargs, 1):

        with open(db_files_list[i], "r") as f_in:
            json_data = json.load(f_in)

            for surrogate_model in json_data["surrogate_model"]:
                merged_json_data["surrogate_model"].append(surrogate_model)
            for func_eval in json_data["func_eval"]:
                merged_json_data["func_eval"].append(func_eval)

    with open("db.out", "w") as f_out:

        json.dump(merged_json_data, f_out, indent=2)

    return

db_files_list =[]
db_files_list.append("TLA_experiments/SLA-GPTune-s-5/xsbench.json")
db_files_list.append("TLA_experiments/SLA-GPTune-sm-5/xsbench.json")
db_files_list.append("TLA_experiments/SLA-GPTune-m-5/xsbench.json")
merge_db(db_files_list)
