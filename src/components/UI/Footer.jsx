import React from "react";
import logo from "../../images/logo-text.png";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer>
      <div className="container">
        <div className="row">
          <div className="col-lg-12">
            <div className="copyright-text">
              <p>Designed & Developed by Team Enemies of Syntaxx</p>
            </div>
          </div>
          <div className="col-lg-3">
            <div className="footer-widget">
              <h4>Team</h4>
              <p>Jay Jain</p>
              <p>Yash Joshi</p>
              <p>Rachana Yeldi</p>
            </div>
          </div>
          <div className="col-lg-3">
            <div className="footer-widget">
              <h4>Useful Links</h4>
              <ul>
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/visualize">Visualize</Link>
                </li>
                <li>
                  <Link to="/build">Build</Link>
                </li>
                {/* <li>
                  <Link to="/discuss">Discuss</Link>
                </li> */}
              </ul>
            </div>
          </div>
          <div className="col-lg-3">
            <div className="footer-widget">
              <h4></h4>
              <br />
              <ul>
                <li>
                  <Link to="/contests">Contests</Link>
                </li>
                <li>
                  <Link to="/explain">Explain</Link>
                </li>
                <li>
                  <Link to="/analyze">Analyze</Link>
                </li>
                {/* <li>
                  <Link to="/profile">Profile</Link>
                </li> */}
              </ul>
            </div>
          </div>
          <div className="col-lg-3">
            <div className="footer-widget">
              <h4>Project</h4>
              <div className="logo">
                <Link to="/">
                  <img src={logo} alt="logo" />
                </Link>
              </div>
              <p>
                Visualizing the learning process to make it more efficient and
                fun
              </p>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
