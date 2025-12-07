def selection_5():

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

    # Creating weights for histo: y6_PT_0
    y6_PT_0_weights = numpy.array([0.0019697290086536385,0.0012516430054988611,0.0005796052025463878,0.00032387850142290005,0.0001960877008614749,0.00013282110058352483,8.7160850382925e-05,6.6458940291975e-05,4.9481440217387516e-05,3.5502810155975e-05,2.9166480128137513e-05,2.2733410099875012e-05,1.542970006778752e-05,1.19955000527e-05,1.1656920051212513e-05,8.0776150354875e-06,7.061867031025001e-06,5.562429024437499e-06,4.643419020399999e-06,4.208099018487501e-06,3.337458014662502e-06,2.5635540112624985e-06,2.4668170108375025e-06,1.6445440072249986e-06,1.8380200080749994e-06,1.0157480044625e-06,1.209224005312501e-06,1.741282007649999e-06,1.209224005312501e-06,5.8042740255e-07,6.771653029749999e-07,5.8042740255e-07,5.320585023375002e-07,6.287964027625001e-07,5.320585023375002e-07,4.83689502125e-07,5.8042740255e-07,4.353206019125002e-07,1.9347580085000002e-07,4.8368950212500005e-08])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PT_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p_{T}$ $[ mu+_{1} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y6_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
