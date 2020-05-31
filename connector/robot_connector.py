import requests


def robot_get_path(robot_name):
    if robot_name not in ['vn', 'swe']:
        print('Wrong robot location. Check')
        return {'Label': 'Bad Request'}
    else:
        r = requests.get('http://localhost:8000/order/')

    # get the oldest one for robot_name where status incomplete to process
    # equals: SELECT * FROM home_order WHERE robot = $robot_name and status = 'incomplete' order by id ASC LIMIT 1;
    result = r.json()
    for i in range(len(result)):
        if result[i]['robot'] == robot_name and result[i]['status'] == 'incomplete':
            return result[i]

    return {'Label': 'Not Found'}


# return true if patch request succeed
# False otherwise
def robot_post_complete(order_id):
    payload = {'status': 'completed'}
    r = requests.patch('http://localhost:8000/order/' + str(order_id) + '/', data=payload)
    if r.status_code == 200:
        return True
    else:
        return False
