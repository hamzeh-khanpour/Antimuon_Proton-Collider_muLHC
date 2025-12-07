void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  TH1F* S6_PT_0 = new TH1F("S6_PT_0","S6_PT_0",40,0.0,500.0);
  // Content
  S6_PT_0->SetBinContent(0,0.0); // underflow
  S6_PT_0->SetBinContent(1,0.002869761090176277);
  S6_PT_0->SetBinContent(2,0.0018522010582015678);
  S6_PT_0->SetBinContent(3,0.0008569159269268017);
  S6_PT_0->SetBinContent(4,0.0004960099155860805);
  S6_PT_0->SetBinContent(5,0.00031149360978803916);
  S6_PT_0->SetBinContent(6,0.0002039619064090789);
  S6_PT_0->SetBinContent(7,0.00014627790459647907);
  S6_PT_0->SetBinContent(8,0.0001011465031783186);
  S6_PT_0->SetBinContent(9,7.966923250344002e-05);
  S6_PT_0->SetBinContent(10,5.6523071776120035e-05);
  S6_PT_0->SetBinContent(11,4.868675152987996e-05);
  S6_PT_0->SetBinContent(12,3.722251116964003e-05);
  S6_PT_0->SetBinContent(13,3.018434094848017e-05);
  S6_PT_0->SetBinContent(14,2.5685710807120068e-05);
  S6_PT_0->SetBinContent(15,1.9228000604199948e-05);
  S6_PT_0->SetBinContent(16,1.6543340519840085e-05);
  S6_PT_0->SetBinContent(17,1.3495880424079987e-05);
  S6_PT_0->SetBinContent(18,1.1827040371640159e-05);
  S6_PT_0->SetBinContent(19,8.997254282720013e-06);
  S6_PT_0->SetBinContent(20,9.360046294119998e-06);
  S6_PT_0->SetBinContent(21,7.763759243959996e-06);
  S6_PT_0->SetBinContent(22,6.67538220976001e-06);
  S6_PT_0->SetBinContent(23,5.514446173280008e-06);
  S6_PT_0->SetBinContent(24,4.353510136800007e-06);
  S6_PT_0->SetBinContent(25,4.4986271413600065e-06);
  S6_PT_0->SetBinContent(26,2.757223086640004e-06);
  S6_PT_0->SetBinContent(27,3.7004831162799894e-06);
  S6_PT_0->SetBinContent(28,1.3786110433199863e-06);
  S6_PT_0->SetBinContent(29,1.6688450524399868e-06);
  S6_PT_0->SetBinContent(30,2.684664084359988e-06);
  S6_PT_0->SetBinContent(31,1.3786110433199863e-06);
  S6_PT_0->SetBinContent(32,1.1609360364800015e-06);
  S6_PT_0->SetBinContent(33,1.5237280478799865e-06);
  S6_PT_0->SetBinContent(34,1.1609360364800015e-06);
  S6_PT_0->SetBinContent(35,1.5237280478799865e-06);
  S6_PT_0->SetBinContent(36,6.530265205200009e-07);
  S6_PT_0->SetBinContent(37,1.3060530410400019e-06);
  S6_PT_0->SetBinContent(38,7.255850228000011e-07);
  S6_PT_0->SetBinContent(39,7.981435250800012e-07);
  S6_PT_0->SetBinContent(40,8.707020273600012e-07);
  S6_PT_0->SetBinContent(41,8.561903269040012e-06); // overflow
  S6_PT_0->SetEntries(100000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ mu+_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
