import axios from "axios";
import { UNIT_LIST_FAIL, UNIT_LIST_REQUEST, UNIT_LIST_SUCCESS } from "./types";

export const listUnits = () => async (dispatch) => {
  try {
    dispatch({
      type: UNIT_LIST_REQUEST,
    });
    const { data } = await axios.get("/api/units/all");

    dispatch({
      type: UNIT_LIST_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: UNIT_LIST_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};
