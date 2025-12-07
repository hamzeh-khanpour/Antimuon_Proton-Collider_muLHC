void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S9_DELTAR_0 = new TH1F("S9_DELTAR_0","S9_DELTAR_0",40,0.0,10.0);
  // Content
  S9_DELTAR_0->SetBinContent(0,0.0); // underflow
  S9_DELTAR_0->SetBinContent(1,0.0);
  S9_DELTAR_0->SetBinContent(2,0.0);
  S9_DELTAR_0->SetBinContent(3,0.0);
  S9_DELTAR_0->SetBinContent(4,0.0);
  S9_DELTAR_0->SetBinContent(5,0.0);
  S9_DELTAR_0->SetBinContent(6,0.0);
  S9_DELTAR_0->SetBinContent(7,0.0);
  S9_DELTAR_0->SetBinContent(8,0.0);
  S9_DELTAR_0->SetBinContent(9,0.0);
  S9_DELTAR_0->SetBinContent(10,0.0);
  S9_DELTAR_0->SetBinContent(11,0.0);
  S9_DELTAR_0->SetBinContent(12,0.0);
  S9_DELTAR_0->SetBinContent(13,0.00014829919389866035);
  S9_DELTAR_0->SetBinContent(14,0.00027560628866097963);
  S9_DELTAR_0->SetBinContent(15,0.000307142787363502);
  S9_DELTAR_0->SetBinContent(16,0.0003234915866908781);
  S9_DELTAR_0->SetBinContent(17,0.0003342777862471112);
  S9_DELTAR_0->SetBinContent(18,0.0003282800864938692);
  S9_DELTAR_0->SetBinContent(19,0.00031671988696948);
  S9_DELTAR_0->SetBinContent(20,0.00030951288726599105);
  S9_DELTAR_0->SetBinContent(21,0.0002950021878629917);
  S9_DELTAR_0->SetBinContent(22,0.0002790404885196895);
  S9_DELTAR_0->SetBinContent(23,0.0002573227894132011);
  S9_DELTAR_0->SetBinContent(24,0.00023705619024701148);
  S9_DELTAR_0->SetBinContent(25,0.0002164026910967397);
  S9_DELTAR_0->SetBinContent(26,0.0001930888920559183);
  S9_DELTAR_0->SetBinContent(27,0.0001761113927544082);
  S9_DELTAR_0->SetBinContent(28,0.00015676379355040898);
  S9_DELTAR_0->SetBinContent(29,0.00013344989450959164);
  S9_DELTAR_0->SetBinContent(30,0.00011700449518618983);
  S9_DELTAR_0->SetBinContent(31,0.00010017209587871002);
  S9_DELTAR_0->SetBinContent(32,8.111472666277013e-05);
  S9_DELTAR_0->SetBinContent(33,6.413722736126004e-05);
  S9_DELTAR_0->SetBinContent(34,5.185151786671987e-05);
  S9_DELTAR_0->SetBinContent(35,3.855004841397021e-05);
  S9_DELTAR_0->SetBinContent(36,2.926321879604984e-05);
  S9_DELTAR_0->SetBinContent(37,2.2685039066689947e-05);
  S9_DELTAR_0->SetBinContent(38,1.668728931344994e-05);
  S9_DELTAR_0->SetBinContent(39,1.214060950050988e-05);
  S9_DELTAR_0->SetBinContent(40,7.64229368558002e-06);
  S9_DELTAR_0->SetBinContent(41,8.077614667670003e-06); // overflow
  S9_DELTAR_0->SetEntries(100000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_DELTAR_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("#DeltaR [ h_{1}, mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
