import React from "react";
import { Link } from "react-router-dom";
import { TOKEN_SERIALIZER } from "../constants";

import useAuth from "../hooks/useAuth";

const Template = ({ children }) => {
  const { user } = useAuth();

  return (
    <React.Fragment>
      <nav className="nav">
        <Link className="nav-link" to="/">
          Menu
        </Link>
        {user && (
          <>
            <Link className="nav-link">
            User: {user.username}
          </Link>
          <Link className="nav-link" onClick={() => {
            window.localStorage.removeItem(TOKEN_SERIALIZER);

            window.location.href = "/"
          }}>
            <span className="badge badge-danger">
              Logout
            </span>
          </Link>
          </>
        )}
      </nav>
      <br />
      <div className="container">{children}</div>
    </React.Fragment>
  );
};

export default Template;
