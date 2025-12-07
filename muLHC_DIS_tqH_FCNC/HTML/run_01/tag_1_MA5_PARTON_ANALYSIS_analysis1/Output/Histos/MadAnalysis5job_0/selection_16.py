def selection_16():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,500.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([6.25,18.75,31.25,43.75,56.25,68.75,81.25,93.75,106.25,118.75,131.25,143.75,156.25,168.75,181.25,193.75,206.25,218.75,231.25,243.75,256.25,268.75,281.25,293.75,306.25,318.75,331.25,343.75,356.25,368.75,381.25,393.75,406.25,418.75,431.25,443.75,456.25,468.75,481.25,493.75])

    # Creating weights for histo: y17_M_0
    y17_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.0172197431600534e-05,0.006318080680318066,0.012666247354351956,0.014561666958448334,0.017735756295464027,0.020217855777018314,0.020684195679612095,0.021812425443954384,0.022233625355976727,0.022760135246002573,0.023602545070045177,0.024098964966356034,0.023557415079471653,0.024174184950644547,0.024490084884661305,0.025543094664715084,0.024098964966356034,0.024189224947503085,0.024098964966356034,0.02373793504176575,0.02358750507318664,0.02349724509203959,0.02312116517059286,0.023151255164307844,0.02301586519258727,0.022007985403107017,0.021782335450239398])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y17_M_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$M$ $[ mu+_{1} t_{1} ]$ $(GeV/c^{2})$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y17_M_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y17_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_16.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_16.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_16.eps')

# Running!
if __name__ == '__main__':
    selection_16()
