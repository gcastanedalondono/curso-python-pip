import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['her', 'invest', 'you']
    values = [80, 5, 15]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.show()
    plt.savefig('your_money.png')
    plt.close()