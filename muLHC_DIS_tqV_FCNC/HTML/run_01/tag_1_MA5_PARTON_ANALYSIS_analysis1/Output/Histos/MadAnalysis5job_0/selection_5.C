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
  S6_PT_0->SetBinContent(1,60.83877131460007);
  S6_PT_0->SetBinContent(2,57.224351236499935);
  S6_PT_0->SetBinContent(3,36.69948079299991);
  S6_PT_0->SetBinContent(4,28.57747061750006);
  S6_PT_0->SetBinContent(5,24.292000524899912);
  S6_PT_0->SetBinContent(6,21.816060471399965);
  S6_PT_0->SetBinContent(7,19.11335041299999);
  S6_PT_0->SetBinContent(8,17.12797037010003);
  S6_PT_0->SetBinContent(9,15.36473033200006);
  S6_PT_0->SetBinContent(10,13.532070292400062);
  S6_PT_0->SetBinContent(11,12.449130268999967);
  S6_PT_0->SetBinContent(12,11.26438024339997);
  S6_PT_0->SetBinContent(13,10.62110022950002);
  S6_PT_0->SetBinContent(14,9.519652205700005);
  S6_PT_0->SetBinContent(15,8.21920417760001);
  S6_PT_0->SetBinContent(16,8.098878175000015);
  S6_PT_0->SetBinContent(17,7.293618157600009);
  S6_PT_0->SetBinContent(18,6.317124136499992);
  S6_PT_0->SetBinContent(19,6.0487051307000135);
  S6_PT_0->SetBinContent(20,5.7293771237999955);
  S6_PT_0->SetBinContent(21,4.993536107899993);
  S6_PT_0->SetBinContent(22,4.692721101400002);
  S6_PT_0->SetBinContent(23,4.553883098399999);
  S6_PT_0->SetBinContent(24,4.2021600907999925);
  S6_PT_0->SetBinContent(25,4.049439087500008);
  S6_PT_0->SetBinContent(26,3.4524360746000062);
  S6_PT_0->SetBinContent(27,3.2904580710999967);
  S6_PT_0->SetBinContent(28,3.2349230699);
  S6_PT_0->SetBinContent(29,2.9665030640999985);
  S6_PT_0->SetBinContent(30,2.730479059000008);
  S6_PT_0->SetBinContent(31,2.4065240520000097);
  S6_PT_0->SetBinContent(32,2.471315053400009);
  S6_PT_0->SetBinContent(33,2.1519870464999915);
  S6_PT_0->SetBinContent(34,2.1890110473000033);
  S6_PT_0->SetBinContent(35,2.050173044300001);
  S6_PT_0->SetBinContent(36,1.7956370388000042);
  S6_PT_0->SetBinContent(37,1.6799390363000095);
  S6_PT_0->SetBinContent(38,1.6336590352999945);
  S6_PT_0->SetBinContent(39,1.545729033400009);
  S6_PT_0->SetBinContent(40,1.5642400337999933);
  S6_PT_0->SetBinContent(41,24.990820539999966); // overflow
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
