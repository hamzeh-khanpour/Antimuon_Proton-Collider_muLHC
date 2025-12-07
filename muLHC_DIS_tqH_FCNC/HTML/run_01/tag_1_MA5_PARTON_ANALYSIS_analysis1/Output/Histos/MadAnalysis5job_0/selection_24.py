def selection_24():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,10.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.125,0.375,0.625,0.875,1.125,1.375,1.625,1.875,2.125,2.375,2.625,2.875,3.125,3.375,3.625,3.875,4.125,4.375,4.625,4.875,5.125,5.375,5.625,5.875,6.125,6.375,6.625,6.875,7.125,7.375,7.625,7.875,8.125,8.375,8.625,8.875,9.125,9.375,9.625,9.875])

    # Creating weights for histo: y25_DELTAR_0
    y25_DELTAR_0_weights = numpy.array([0.0017600367873993072,0.00532524035674652,0.010154058773457495,0.014275858275571636,0.019270147672294822,0.025693526896393495,0.0332601859823916,0.04192498493574174,0.05417002345662284,0.07001036154321576,0.08887433926457321,0.116087185977443,0.14021628306280917,0.10773828698593425,0.09943456798896808,0.088648699291829,0.08391013986421533,0.07655408075277817,0.06841579173582915,0.06306047238271596,0.05496730336031675,0.047505954261597906,0.04079675507202437,0.03356104594604972,0.0288074465202528,0.022715007256178782,0.018352517783138386,0.014501498248315833,0.01024431876255469,0.007852472051473804,0.005641144318587431,0.0032342556093235162,0.002873222652933887,0.001624649803753151,0.0011884008564491111,0.0007220664127791983,0.0004061623509382998,0.0001805165781948026,0.00012034438546320172,6.0172202731599655e-05])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y25_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ mu+_{1}, t_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y25_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y25_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_24.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_24.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_24.eps')

# Running!
if __name__ == '__main__':
    selection_24()
