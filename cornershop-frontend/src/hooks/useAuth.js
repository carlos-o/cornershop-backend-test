import { useContext } from "react";

import { UserContext } from "../components/User";

export default function useAuth() {
  return useContext(UserContext);
}
