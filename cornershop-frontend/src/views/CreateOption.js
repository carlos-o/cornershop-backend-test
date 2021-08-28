import React, { useState } from "react";
import { useParams, useHistory } from "react-router-dom";

import Template from "../components/Template";
import { API_URL, TOKEN_SERIALIZER } from "../constants";

const CreateOption = () => {
  const [description, setDescription] = useState("");

  const { id } = useParams();

  const history = useHistory();

  const handleChangeDescription = (e) => {
    setDescription(e.target.value);
  };

  const handleSubmitDescription = async (e) => {
    e.preventDefault();

    try {
      await fetch(`${API_URL}/menu/${id}/option/`, {
        body: JSON.stringify({
          description,
        }),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
        },
      });

      history.goBack();
    } catch (err) {
      console.log("err", err);
    }
  };

  return (
    <Template>
      <hr />
      <br />
      <button className="btn btn-info btn-md" onClick={() => history.goBack()}>
        Volver
      </button>
      <br />
      <br />
      <h1>Crear Opción</h1>
      <br />
      <form className="form-group" onSubmit={handleSubmitDescription}>
        <input
          className="form-control w-50"
          type="text"
          name="description"
          onChange={handleChangeDescription}
          placeholder="Crear descripción"
          value={description}
        />
        <br />
        <button className="btn btn-md bg-success text-white w-50" type="submit">
          Crear Opción
        </button>
      </form>
    </Template>
  );
};

export default CreateOption;
