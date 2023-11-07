from bokeh.plotting import figure, output_file, show


# Punto de entrada
if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()
    type(figure)
    
    total_values = int(input('How many values do you want to graph? '))
    x_values = list(range(total_values))
    y_values = []

    for x in x_values:
        value = int(input(f'Provide the value y for x {x}: '))
        y_values.append(value)

    fig.line(x_values, y_values, line_width=2)
    show(fig)
