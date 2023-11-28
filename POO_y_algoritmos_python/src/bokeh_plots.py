from bokeh.plotting import figure, output_file, show
import random


if __name__ == "__main__":
    output_file("bokeh_graphs.html")
    fig = figure()
    values_to_graph = 13
    #creamos una lista con 13 valores para X
    x_values = list(range(values_to_graph))
    y_values = []
    
    for i in x_values:
        value = random.randint(0,100)
        y_values.append(value)
    
    #hacer la grafica    
    fig.line(x_values, y_values, line_width = 2) 
    #mostrar la grafica
    show(fig)
    