def selection_18():

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

    # Creating weights for histo: y19_M_0
    y19_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.04655824195299962,0.07993876618360025,0.07404188720280085,0.3327974424801918,0.08548965522419963,0.05558407039299988,0.04904034152400025,0.0432788525198004,0.04005964307619984,0.03509543393420029,0.03291419431119984,0.030025924810400513,0.027934945171799765,0.025317455624199573,0.025497965593000712,0.022730046071400424,0.021120446349599278,0.020729326417199392,0.018638336778600374,0.01826226684359928,0.01755523696580041,0.01612614721280041,0.015238607366200392,0.014351067519600373,0.013974997584599285,0.013057367743199938,0.012365387862799867,0.011643317987600467,0.011583147998000086,0.010876128120199486])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y19_M_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$M$ $[ h_{1} p_{1} ]$ $(GeV/c^{2})$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y19_M_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y19_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_18.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_18.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_18.eps')

# Running!
if __name__ == '__main__':
    selection_18()
