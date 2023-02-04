import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo from "../../images/logo-text.png";

const Header = () => {
  const [card, setCard] = useState([]);
  // let token = sessionStorage.getItem("token");
  // useEffect(() => {
  //   (async () => {
  //     let profile_info;
  //     try {
  //       let response = await fetch(
  //         "https://hacknova2.pythonanywhere.com/login/profilecreate/",
  //         {
  //           method: "GET",
  //           headers: {
  //             Authorization: `Token ${token}`,
  //             "Content-Type": "application/json",
  //             Accept: "application/json",
  //           },
  //         }
  //       );
  //       profile_info = await response.json();
  //       console.log(profile_info);
  //     } catch (error) {
  //       console.log("Error" + error);
  //       profile_info = [];
  //     }
  //     setCard(profile_info);
  //   })();
  // }, [token]);
  // console.log(card);

  return (
    <header
      className="header-area header-sticky wow slideInDown"
      data-wow-duration="0.75s"
      data-wow-delay="0s"
    >
      <div className="container">
        <div className="row">
          <div className="col-12">
            <nav className="main-nav">
              <Link to="/" className="logo">
                <img src={logo} alt="logo" />
              </Link>
              <ul className="nav">
                <li className="scroll-to-section">
                  <Link to="/home" className="active">
                    Home
                  </Link>
                </li>
                <li className="scroll-to-section">
                  <Link to="/build">Build</Link>
                </li>
                <li className="scroll-to-section">
                  <Link to="/visualize">Visualize</Link>
                </li>
                {/* <li className="scroll-to-section">
                  <Link to="/explain">Explain</Link>
                </li> */}
                {/* <li className="scroll-to-section">
                  <Link to="/discuss">Discuss</Link>
                </li> */}
                <li className="scroll-to-section">
                  <Link to="/contests">Contests</Link>
                </li>
                <li className="scroll-to-section">
                  <Link to="/analyze">Analyze</Link>
                </li>
                {/* {card.map((post, index) => {
                  return (
                    <Link to="/profile" key={index}>
                      <img
                        src={post.profile_pic}
                        alt=""
                        style={{ height:"50px", width:"40px", borderRadius:"40px" }}
                      />
                    </Link>
                  );
                })} */}
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
