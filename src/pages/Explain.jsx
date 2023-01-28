import React, { useState } from "react";

const Explain = () => {
  const [code, setCode] = useState([]);
  const [values, setValues] = useState({
    text: "",
  });

  const handleChanges = (event) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value,
    });
    console.log(values);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // console.log({
    //   text: data.get("text"),
    // });
    createcode();
  };

  async function createcode() {
    try {
      var formdata = new FormData();
      formdata.append("text", `${values.text}`);

      var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow",
      };

      fetch(
        "http://csvshow.pythonanywhere.com/visualapp/codetoenglish",
        requestOptions
      )
        .then((response) => response.text())
        .then((result) => {
          // console.log(result);
          setCode(result);
        });
    } catch (error) {
      // console.log("Error" + error);
      setCode("No explaination found");
    }
  }

  return (
    <div className="text-input">
      <form
        className="mt-5 mb-5 login-input"
        onSubmit={handleSubmit}
        style={{ margin: "15rem 10rem" }}
      >
        <h3 style={{ margin: "4rem 0 0 0" }}>
          Enter the code here and understand the explaination
        </h3>
        <div
          className="form-group"
          style={{
            display: "flex",
            justifyContent: "space-evenly",
            alignItems: "center",
          }}
        >
          <textarea
            id="exampleFormControlTextarea1"
            rows="7"
            className="form-control"
            placeholder="Enter Code..."
            label="Text"
            name="text"
            value={values.text}
            onChange={handleChanges}
            autoFocus
            required
            style={{ marginTop: "1rem", width: "400px" }}
          />
          {/* <textarea
            id="code"
            style={{ height: "200px", width: "400px", marginTop: "1rem" }}
            value={code}
            placeholder="Explaination"
            readOnly
          ></textarea> */}
          <i className="fa fa-arrow-right"></i>
          <div
            id="code"
            style={{ height: "200px", width: "400px", marginTop: "1rem" }}
          >
            {code}
          </div>
        </div>
        <button
          className="btn btn-info"
          type="submit"
          style={{ marginTop: "5rem" }}
        >
          Explain it!
        </button>
      </form>
    </div>
  );
};

export default Explain;
