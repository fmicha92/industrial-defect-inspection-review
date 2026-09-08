import { BrowserRouter, Route, Routes } from "react-router-dom";
import { ErrorScreen, LoadingScreen, SiteLayout } from "./components/Layout";
import { useSiteData } from "./lib/site-data";
import DatasetsPage from "./pages/DatasetsPage";
import EvidencePage from "./pages/EvidencePage";
import HomePage from "./pages/HomePage";
import ReviewPage from "./pages/ReviewPage";

export default function App() {
  const resource = useSiteData();
  if (resource.status === "loading") return <LoadingScreen />;
  if (resource.status === "error") return <ErrorScreen message={resource.message} />;
  return (
    <BrowserRouter basename={import.meta.env.BASE_URL}>
      <SiteLayout meta={resource.data.meta}>
        <Routes>
          <Route path="/" element={<HomePage data={resource.data} />} />
          <Route path="/datasets" element={<DatasetsPage data={resource.data} />} />
          <Route path="/evidence" element={<EvidencePage data={resource.data} />} />
          <Route path="/review" element={<ReviewPage data={resource.data} />} />
          <Route path="*" element={<HomePage data={resource.data} />} />
        </Routes>
      </SiteLayout>
    </BrowserRouter>
  );
}
