from pandas import DataFrame


def start():
    print("import successful")


class Group:
    count = 0
    pos = 0

    def __init__(self, count):
        self.count = count

    def reset(self):
        self.pos = 0

    def next(self):
        self.pos = self.pos + 1
        return int(self.pos / self.count)


class GroupWithValue:
    count = 0
    pos = 0
    tmp_count = 0
    tmp_value = None

    def __init__(self, count):
        self.count = count

    def reset(self):
        self.pos = 0

    def next(self, value):
        print("sss" + str(value))
        if self.tmp_value is None:
            self.tmp_value = value
        self.tmp_count = self.tmp_count + 1
        if self.tmp_count >= self.count:
            if self.tmp_value != value:
                self.pos = self.pos + 1
                self.tmp_count = 0
                self.tmp_value = value
        return self.pos


def split_by_count(df, index_name, size):
    new_pd = df.sort_values(index_name)
    g = Group(size)
    return new_pd.apply(lambda x: g.next(), axis=1)


def split_by_value(df, index_name, size):
    new_pd = df.sort_values(index_name)
    g = GroupWithValue(size)
    return new_pd.apply(lambda x: g.next(x[index_name]), axis=1)
