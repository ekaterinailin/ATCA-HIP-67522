import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # make a figure and set the aspect ratio to 1
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect(1)
    ax.axis('off')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1.1,0.9)

    # plot the circle
    t = np.linspace(0,2*np.pi,100)
    x = 0.7 * np.cos(t)
    y = 0.7 * np.sin(t)
    ax.plot(x,y,color='grey')

    # time critical parts
    masks = [(360,340),[200,180]]

    # plot time critical parts in orange
    for ma, mi in masks:
        mask = np.where((t<ma/180*np.pi) & (t>mi/180*np.pi))
        ax.plot(x[mask],y[mask],color='orange', linewidth=10)

    # random phase ranges of about 11h each, i.e. 23 deg
    masks = [(x, x-23) for x in [340, 310, 90, 260, 30, 160, 55, 125]]

    # plot random phase ranges in blue
    for ma, mi in masks:
        mask = np.where((t<ma/180*np.pi) & (t>mi/180*np.pi))
        ax.plot(x[mask],y[mask],color='blue', linewidth=5)

    # plot the pilot observations in magenta
    mask = np.where((t<220/180*np.pi) & (t>200/180*np.pi))
    ax.plot(x[mask],y[mask],color='magenta', linewidth=15)

    # plot the phase range where flares cluster in red
    mask = np.where((t<295*np.pi/180) & (t>275*np.pi/180))
    ax.plot(x[mask],y[mask],color='red', linewidth=20, zorder=-10)

    # plot the central point
    plt.scatter([0],[0],color='black',s=200)

    # add text to the cenral point saying HIP 67522
    plt.text(0,0.1,'HIP 67522', fontsize=15, ha='center', va='center')

    # add text to the circle saying orbit of HIP 67522 b
    plt.text(0.4,0.8,'orbit of HIP 67522 b', fontsize=15, ha='center', va='center')
    plt.plot([0.4,0.7*np.cos(np.pi/3)],[0.75,0.7*np.sin(np.pi/3)],color='black', linewidth=1)

    # add a manual legend with handles, where orange are time critical parts, blue are non-time critical parts
    # and red is the part where flares cluster in orbital phase
    handles = [plt.Line2D([0],[0],color='orange', linewidth=5),
            plt.Line2D([0],[0],color='magenta', linewidth=5),
            plt.Line2D([0],[0],color='blue', linewidth=5),
            plt.Line2D([0],[0],color='red', linewidth=5)]

    labels = ['phase ranges at quadrature of HIP 67522 b',
            'pilot observations and detection of HIP 67522 in Stokes V with ATCA in Dec 2023',
            'randomly distributed phase ranges',
            'phase range of flares clustering in TESS/planned CHEOPS observations']

    plt.legend(handles, labels, loc='lower left', fontsize=13, frameon=False)

    plt.tight_layout()

    # save the figure
    plt.savefig('phase_coverage.png', dpi=300)