def selection_7():

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

    # Creating weights for histo: y8_PT_0
    y8_PT_0_weights = numpy.array([0.007626826894739919,0.021331046908759702,0.03497509493149946,0.04600164333356051,0.054892092045179613,0.059209441419520475,0.06471520062164006,0.06516649055624028,0.06423382069140039,0.06286491088977927,0.061706591057639995,0.05856259151326029,0.05465140208005978,0.05180826249208024,0.0503641327013598,0.04463273353193938,0.04219575388510019,0.0405560641227198,0.03753241456089929,0.0349901349293199,0.032312475317359424,0.030552435572419843,0.029093255783880414,0.02692705609780049,0.025257286339779212,0.023858276542520106,0.022218586780139715,0.02160181686952042,0.018848937268460632,0.017991487392720055,0.01823217735783989,0.017118987519160488,0.015629727734980173,0.01585537770227956,0.014351067920280253,0.01367412801838064,0.012801638144819622,0.011432718343199947,0.010921258417319401,0.010439878487079739])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y8_PT_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p_{T}$ $[ t_{1} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y8_PT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y8_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_7.eps')

# Running!
if __name__ == '__main__':
    selection_7()
