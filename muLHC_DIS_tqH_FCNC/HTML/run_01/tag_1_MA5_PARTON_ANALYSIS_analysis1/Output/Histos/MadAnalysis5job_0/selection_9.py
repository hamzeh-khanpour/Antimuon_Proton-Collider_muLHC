def selection_9():

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

    # Creating weights for histo: y10_PT_0
    y10_PT_0_weights = numpy.array([0.010424838274429235,0.02779955539848017,0.04403100271177077,0.05611058071229931,0.06435416934777977,0.06921306854351075,0.07256767798823921,0.07309417790109035,0.06775389878503973,0.06695661891700944,0.062248139696380204,0.05629109068242041,0.05435054100362978,0.05185339141697033,0.04729535217143951,0.04448230263706938,0.03974373342142078,0.03921723350856964,0.03523082416841983,0.03405746436264014,0.03219212467140039,0.029785235069800655,0.02734826547317991,0.02546788578442965,0.024550255936320275,0.023000826192789547,0.021541646434320195,0.02100009652396021,0.01901441685263973,0.018713556902439556,0.016652657243569853,0.015674857405420115,0.014787317552330101,0.014396197617070205,0.012921977861090346,0.011432718107599984,0.011327418125029758,0.01080090821218028,0.009913370359089933,0.008709925558290066])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_PT_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p_{T}$ $[ h_{1} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y10_PT_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y10_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_9.eps')

# Running!
if __name__ == '__main__':
    selection_9()
