from collections import Counter

data = [{"user": "Amit", "action": "login"},
        {"user": "Sitaram", "action": "purchase"},
        {"user": "Amit", "action": "purchase"},
        {"user": "Sitaram", "action": "login"},
        {"user": "Sitaram", "action": "logout"},
        {"user": "Amit", "action": "purchase"},
        {"user": "Amit", "action": "purchase"}]

"""Output: summary:
count per user
total actions
unique actions
top user"""

# filter
# use user and action field for filter


def user_action_summary(log_data):
    # collection
    summary = {}

    def total_action_size():
        # data transformation for total action
        return len(log_data)

    def unique_actions_list():
        # data transformation for unique actions
        unique_actions = set([record.get('action', None)
                             for record in log_data])
        return unique_actions

    def user_action_count():
        # actions_count = Counter(record['user'] for record in log_data)
        # container to collect the actions per user data
        actions_count = {}
        # action per user data transform/extraction
        for record in log_data:
            name = record['user']
            actions_count[name] = actions_count.get(name, 0) + 1
        return actions_count

    def top_user_filter(action_data):
        # extract top user data
        top_user = max(action_data, key=lambda k: action_data[k])
        return top_user

    summary['total_actions'] = total_action_size()
    summary['actions_count'] = unique_actions_list()
    summary['unique_actions'] = user_action_count()
    summary['top_user'] = top_user_filter(summary['unique_actions'])
    return summary


print(user_action_summary(data))
