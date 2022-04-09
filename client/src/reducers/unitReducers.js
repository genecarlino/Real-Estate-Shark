import {
  UNIT_LIST_FAIL,
  UNIT_LIST_REQUEST,
  UNIT_LIST_SUCCESS,
} from "../actions/types";

export const unitsListReducer = (state = { units: [] }, action) => {
  switch (action.type) {
    case UNIT_LIST_REQUEST:
      return { loading: true, units: [] };
    case UNIT_LIST_SUCCESS:
      return { loading: false, units: action.payload.results };
    case UNIT_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};
