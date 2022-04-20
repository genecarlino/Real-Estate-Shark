import logo from './logo.svg';
import './App.css';
import UnitPost from './UnitPost'
import Navbar from './Navbar';
import HomePage from './HomePage'
import UnitInfo from './UnitInfo'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="content">
          <Switch>
            <Route exact path="/">
              <HomePage />
            </Route>
            <Route path="/create">
              <UnitPost />
            </Route>
              <Route path="/unit/:id">
                <UnitInfo />
            </Route>
          </Switch>
      </div>
    </Router>
  );
}

export default App;
