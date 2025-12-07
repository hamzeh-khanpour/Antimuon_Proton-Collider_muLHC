def selection_26():

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

    # Creating weights for histo: y27_DELTAR_0
    y27_DELTAR_0_weights = numpy.array([0.00902582979272005,0.029890542690223825,0.04452742911075173,0.054591226649635234,0.0642187742952043,0.07187569242269372,0.07861497077459327,0.08955126810010568,0.1000663755286207,0.12102137040404587,0.14409736476077753,0.17603375695068585,0.19343855269431745,0.10305997479653159,0.06695661362566166,0.04705465849271406,0.033636261774202716,0.02415913409184823,0.01699864584295616,0.011116817281365984,0.007747170105418156,0.005926961550552836,0.003911193043511989,0.0025874043672464565,0.0013990036578715981,0.0008875398829508163,0.0007972816050236109,0.0004813775822784043,0.0003008610264239935,0.00016547355953319765,6.0172195284801147e-05,3.0086102642399354e-05,4.5129148963600245e-05,0.0,0.0,1.5043046321200898e-05,0.0,1.5043046321200898e-05,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y27_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ p_{1}, t_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y27_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y27_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_26.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_26.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_26.eps')

# Running!
if __name__ == '__main__':
    selection_26()
