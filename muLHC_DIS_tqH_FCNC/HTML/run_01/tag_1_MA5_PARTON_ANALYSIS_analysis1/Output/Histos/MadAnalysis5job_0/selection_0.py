def selection_0():

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

    # Creating weights for histo: y1_THT_0
    y1_THT_0_weights = numpy.array([0.33020994665907705,0.24911295975919165,0.16350287358833596,0.12004358060859328,0.08672318599104956,0.059811170338319425,0.04463273279018944,0.032297424782790574,0.026430635730490502,0.023331766231070694,0.018397647028110503,0.016667697307560337,0.015990757416910764,0.014095337723090021,0.012771547936930245,0.012064528051139684,0.012079568048710177,0.011267248179929397,0.010394748320869875,0.010635438281989687,0.010169098357320557,0.008935571556580021,0.00923643250798003,0.008409064641630049,0.008394021644060041,0.008544452619759965,0.0075967407728499145,0.008228548670789948,0.00803298870238,0.007882558726679914,0.006844587894349976,0.0072507498287400435,0.006558769940519976,0.006423381962390063,0.006408338964820054,0.00579157406445003,0.00559601509603992,0.00568627308145997,0.005069508181089946,0.0049942921932400654])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_THT_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$H_{T}$ $(GeV)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_THT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y1_THT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_0.eps')

# Running!
if __name__ == '__main__':
    selection_0()
