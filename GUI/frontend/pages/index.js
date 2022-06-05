import React, { useState, useEffect } from "react";
import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";

export default function Home() {
  const defaultState = {
    isLoading: false,
    result: "",
  };
  const defaultFormData = {
    knownData: "ph",
    data: "0",
    predictingData: "ph",
  };
  const [state, setState] = useState(defaultState);
  const [formData, setFormData] = useState(defaultFormData);
  useEffect(() => {
    console.log(formData);
  }, [formData, state]);
  const handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    if (name === "knownData") {
      setFormData((prevState) => {
        return { ...prevState, knownData: value };
      });
    }
    if (name === "predictingData") {
      setFormData((prevState) => {
        return { ...prevState, predictingData: value };
      });
    }
    if (name === "data") {
      setFormData((prevState) => {
        return { ...prevState, data: value };
      });
    }
  };

  const handlePredictClick = (event) => {
    if (formData.knownData === formData.predictingData) {
      setState((prevState) => {
        return {
          ...prevState,
          result: `Sorry we cannot predict ${formData.knownData} with ${formData.predictingData}`,
          isLoading: false,
        };
      });
      return null;
    }
    setState((prevState) => {
      return { ...prevState, isLoading: true };
    });
    const headers = {
      "Content-Type": "text/plain",
    };
    const url = `http://127.0.0.1:5000/${formData.knownData}/${formData.predictingData}`;
    axios.post(url, formData, { headers }).then((response) => {
      console.log(response);
      setState((prevState) => {
        const { val, MAE } = response.data;
        let result = `The value of ${formData.predictingData} is ${val} using ${formData.knownData} with a mean absolute error of ${MAE}`;
        return { ...prevState, result: result, isLoading: false };
      });
    });
  };

  const handleCancelClick = (event) => {
    setState((prevState) => {
      return { ...prevState, ...defaultState };
    });
    setFormData((prevState) => {
      return { ...prevState, ...defaultFormData };
    });
  };
  const isLoading = state.isLoading;
  const result = state.result;
  return (
    <Container>
      <div>
        <h1 className="title">Predict what your plant needs</h1>
      </div>
      <div className="content">
        <Form>
          <Form.Row>
            <Form.Group as={Col}>
              <Form.Label>Known Value</Form.Label>
              <Form.Control
                as="select"
                value={formData.knownData}
                name="knownData"
                onChange={handleChange}
              >
                <option value="ph">PH</option>
                <option value="temperature">TEMPERATURE</option>
                <option value="humidity">HUMIDITY</option>
                <option value="sunlight">SUNLIGHT</option>
                <option value="waterlevel">WATER LEVEL</option>
                <option value="soilmoisture">SOIL MOISTURE</option>
              </Form.Control>
            </Form.Group>
            <Form.Group as={Col}>
              <Form.Label>Value</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter value"
                name="data"
                value={formData.data}
                onChange={handleChange}
              />
            </Form.Group>
          </Form.Row>
          <Form.Group as={Col}>
            <Form.Label>Value to Predict</Form.Label>
            <Form.Control
              as="select"
              value={formData.predictingData}
              name="predictingData"
              onChange={handleChange}
            >
              <option value="ph">PH</option>
              <option value="temperature">TEMPERATURE</option>
              <option value="humidity">HUMIDITY</option>
              <option value="sunlight">SUNLIGHT</option>
              <option value="waterlevel">WATER LEVEL</option>
              <option value="soilmoisture">SOIL MOISTURE</option>
            </Form.Control>
          </Form.Group>
          <Row>
            <Col>
              <Button
                block
                variant="success"
                disabled={isLoading}
                onClick={!isLoading ? handlePredictClick : null}
              >
                {isLoading ? "Making prediction" : "Predict"}
              </Button>
            </Col>
            <Col>
              <Button
                block
                variant="danger"
                disabled={isLoading}
                onClick={handleCancelClick}
              >
                Reset prediction
              </Button>
            </Col>
          </Row>
        </Form>
        {result === "" ? null : (
          <Row>
            <Col className="result-container">
              <h5 id="result">{result}</h5>
            </Col>
          </Row>
        )}
      </div>
    </Container>
  );
}
