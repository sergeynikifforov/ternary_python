import ternary

def H2_mol(x,y=1):
    if(y>=1):
        return (2*y-2)/(3.76+x+2*y)*100
    if(y<1):
        return 0
def Air_mol(x,y=1):
    if(y>=1):
        return (3.76)/(3.76+x+2*y)*100
    if(y<1):
        return (4.76-y)/(4.76+x+y)*100
def H2O_mol(x,y=1):
    if(y>=1):
        return (2+x)/(3.76+x+2*y)*100
    if(y<1):
        return (2*y+x)/(4.76+x+y)*100

alpha = 0.
ER = 1.0


array_new = list()
for i in range(1,100):
    b = list()
    b.append(Air_mol(alpha,ER))
    b.append(H2O_mol(alpha,ER))
    b.append(H2_mol(alpha,ER))
    alpha += alpha + float(i)/100
    array_new.append(b)

figure, tax = ternary.figure(scale=100.0)
tax.boundary(linewidth=2)
tax.gridlines(color="black", multiple=5)
tax.gridlines(color="blue", multiple=5, linewidth=0.5)

fontsize = 20
tax.left_axis_label("AIR", fontsize=fontsize)
tax.right_axis_label("H2", fontsize=fontsize)
tax.bottom_axis_label("H2O", fontsize=fontsize)
tax.set_title("AIR_H2O_H2", fontsize=20)
tax.plot(array_new, linewidth=2.0, label="Curve")
# Set ticks
tax.ticks(axis='lbr', multiple=5, linewidth=1)

# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()

ternary.plt.show()
