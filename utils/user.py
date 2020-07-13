import pandas as pd


class User:
    def __init__(self, data):
        self.data = {key: data[key] for key in data.keys() if key != 'ldap' or key != 'password'}
        try:
            if self.data['s1'] == 'on':
                self.data['s1'] = "True"
        except:
            self.data['s1'] = "False"

        try:
            if self.data['s2'] == 'on':
                self.data['s2'] = "True"
        except:
            self.data['s2'] = "False"

    def save(self):
        try:
            df = pd.read_csv('userData.csv', index_col=None)
            df = df.append(dict(self.data), ignore_index=True)
            df.to_csv('userData.csv', index=False)
        except:
            df = pd.DataFrame(dict(self.data), index=[0])
            df.to_csv('userData.csv', index=False)