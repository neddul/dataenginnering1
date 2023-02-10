import matplotlib.pyplot as plt

def read_data(file_name):
    with open(file_name, 'r') as f:
        data = {}
        for line in f:
            char, count = line.strip().split()
            data[char] = int(count)
    return data

def plot_data(data):
    plt.bar(data.keys(), data.values())
    plt.xlabel('Character')
    plt.ylabel('Count')
    plt.title('Character Counts')
    plt.savefig('char_counts.pdf', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    file_name = 'part-r-00000'
    data = read_data(file_name)
    plot_data(data)
