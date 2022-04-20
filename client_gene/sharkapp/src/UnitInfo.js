import { useParams } from "react-router-dom";
import useFetch from "./useFetch";

const UnitInfo = () => {
    const { id } = useParams();
    const { data: unit, error, isPending} = useFetch('http://localhost:202/unitmanagement/unit/' + String(id) + '/');
  
    console.log(unit)
    return (
      <div className="home">
        {unit && (
        <h2>{unit.unit.zip}</h2>)}
      </div>
    );
  }
   
  export default UnitInfo;