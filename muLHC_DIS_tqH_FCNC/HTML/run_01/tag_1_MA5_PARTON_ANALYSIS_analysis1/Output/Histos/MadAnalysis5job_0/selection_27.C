void selection_27()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo55","canvas_plotflow_tempo55",0,0,700,500);
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
  TH1F* S28_DELTAR_0 = new TH1F("S28_DELTAR_0","S28_DELTAR_0",40,0.0,10.0);
  // Content
  S28_DELTAR_0->SetBinContent(0,0.0); // underflow
  S28_DELTAR_0->SetBinContent(1,0.009612509161405259);
  S28_DELTAR_0->SetBinContent(2,0.02462547528985943);
  S28_DELTAR_0->SetBinContent(3,0.03274872373611715);
  S28_DELTAR_0->SetBinContent(4,0.0378483127607134);
  S28_DELTAR_0->SetBinContent(5,0.04224088192054207);
  S28_DELTAR_0->SetBinContent(6,0.047490910916363496);
  S28_DELTAR_0->SetBinContent(7,0.054380619598561664);
  S28_DELTAR_0->SetBinContent(8,0.0633161978894442);
  S28_DELTAR_0->SetBinContent(9,0.07510994563364166);
  S28_DELTAR_0->SetBinContent(10,0.09341734213196667);
  S28_DELTAR_0->SetBinContent(11,0.12970117519191976);
  S28_DELTAR_0->SetBinContent(12,0.2084816601234935);
  S28_DELTAR_0->SetBinContent(13,0.3264642375568418);
  S28_DELTAR_0->SetBinContent(14,0.14077287307422445);
  S28_DELTAR_0->SetBinContent(15,0.07500464565378251);
  S28_DELTAR_0->SetBinContent(16,0.04864922069481237);
  S28_DELTAR_0->SetBinContent(17,0.029830364294314834);
  S28_DELTAR_0->SetBinContent(18,0.020157686144418163);
  S28_DELTAR_0->SetBinContent(19,0.013192757476607397);
  S28_DELTAR_0->SetBinContent(20,0.010139018060699346);
  S28_DELTAR_0->SetBinContent(21,0.00657381274261992);
  S28_DELTAR_0->SetBinContent(22,0.004573087125300814);
  S28_DELTAR_0->SetBinContent(23,0.0028581794533130084);
  S28_DELTAR_0->SetBinContent(24,0.0024369745338773167);
  S28_DELTAR_0->SetBinContent(25,0.0014290897266565042);
  S28_DELTAR_0->SetBinContent(26,0.0010379708014662326);
  S28_DELTAR_0->SetBinContent(27,0.0007671955532576992);
  S28_DELTAR_0->SetBinContent(28,0.0004813776079263984);
  S28_DELTAR_0->SetBinContent(29,0.0002707748482086099);
  S28_DELTAR_0->SetBinContent(30,0.00016547356834969645);
  S28_DELTAR_0->SetBinContent(31,0.00015043047122700548);
  S28_DELTAR_0->SetBinContent(32,9.025830273619946e-05);
  S28_DELTAR_0->SetBinContent(33,9.025830273619946e-05);
  S28_DELTAR_0->SetBinContent(34,7.521524561350083e-05);
  S28_DELTAR_0->SetBinContent(35,3.0086104245399184e-05);
  S28_DELTAR_0->SetBinContent(36,3.0086104245399184e-05);
  S28_DELTAR_0->SetBinContent(37,3.0086104245399184e-05);
  S28_DELTAR_0->SetBinContent(38,1.5043047122700547e-05);
  S28_DELTAR_0->SetBinContent(39,0.0);
  S28_DELTAR_0->SetBinContent(40,1.5043047122700547e-05);
  S28_DELTAR_0->SetBinContent(41,0.0); // overflow
  S28_DELTAR_0->SetEntries(100000);
  // Style
  S28_DELTAR_0->SetLineColor(9);
  S28_DELTAR_0->SetLineStyle(1);
  S28_DELTAR_0->SetLineWidth(1);
  S28_DELTAR_0->SetFillColor(9);
  S28_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_56","mystack");
  stack->Add(S28_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ t_{1}, h_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_27.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_27.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_27.eps");

}
