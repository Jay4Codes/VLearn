import "./App.css";
import React, { useEffect } from "react";

import Header from "./components/UI/Header";
import Footer from "./components/UI/Footer";
import ScrollToTop from "./components/UI/ScrollToTop";

// import Login from "./pages/Login";
// import Signup from "./pages/Signup";
// import LoginSignupHeader from "./components/UI/LoginSignupHeader";

import Home from "./pages/Home";
import Profile from "./pages/Profile";
import NoMatch from "./pages/NoMatch";

import Build from "./pages/Build";

import Visualize from "./pages/Visualize";

import Visualisations from "./components/Visualize/Visualisations";

import Explain from "./pages/Explain";

import Contests from "./pages/Contests";

import alanBtn from "@alan-ai/alan-sdk-web";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// import Discussion from "./pages/Discussion";
// import CommentGet from "./components/Discuss/CommentGet";
// import CommentPost from "./components/Discuss/CommentPost";

import Analyze from "./pages/Analyze";

function App() {
  useEffect(() => {
    alanBtn({
      key: "3b12133609113b0c558d934a3769129c2e956eca572e1d8b807a3e2338fdd0dc/stage",
    });
  }, []);

  return (
    <div className="App">
      <Router>
        <Header />
        <ScrollToTop />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="*" element={<NoMatch />} />

          <Route path="/build" element={<Build />} />
          <Route path="/visualize" element={<Visualize />} />

          {/* <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} /> */}

          {/* <Route path="/discuss" element={<Discussion />} /> */}
          {/* <Route
            path="/comments/:id"
            element={
              <><Header/>
                <CommentPost />
                <CommentGet />
            }
          /> */}

          <Route
            path="/visualize/sorting"
            element={<Visualisations param="bblsort" />}
          />

          <Route path="/contests" element={<Contests />} />
          <Route path="/analyze" element={<Analyze />} />
          <Route path="/explain" element={<Explain />} />
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
