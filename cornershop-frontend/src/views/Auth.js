import React, { useState } from "react";
import { useHistory } from "react-router-dom";

import Template from "../components/Template";
import { API_URL, TOKEN_SERIALIZER } from "../constants";

import useDispatcher from "../hooks/useDispatcher";

const Auth = () => {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const history = useHistory();

  const dispatcher = useDispatcher();

  /**
   * @description
   * Access to login.
   */
  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const login = await fetch(`${API_URL}/accounts/signin/`, {
        body: JSON.stringify(form),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      const user = await login.json();

      if (user.code == 200){
      dispatcher((state) => ({
            ...state,
            user: user.data,
          }));

          history.push("/account");

          localStorage.setItem(TOKEN_SERIALIZER, user.data.token);
      }else{
        return window.alert(user.errors);
      }
    } catch (e) {
      console.log("err", e);
    }
  };

  const handleChange = ({ target }) => {
    setForm((form) => ({
      ...form,
      [target.name]: target.value,
    }));
  };

  return (
    <Template>
      <div className="row">
        <div className="col-md-4">
          <form className="form-group" onSubmit={handleLogin}>
            <input
              className="form-control"
              name="username"
              onChange={handleChange}
              value={form.username}
              type="text"
              placeholder="Username..."
            />
            <br />
            <input
              className="form-control"
              name="password"
              onChange={handleChange}
              value={form.password}
              type="password"
              placeholder="Password..."
            />
            <br />
            <button className="btn btn-sm bg-primary text-white" type="submit">
              Login
            </button>
          </form>
        </div>
      </div>
    </Template>
  );
};

export default Auth;
