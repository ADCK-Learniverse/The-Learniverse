import './Loader.style.css';
import Navbar from '../Navbar/Navbar';

export default function Loader() {
    return (
        <div className="loader-overlay">
            <Navbar location="loading" />
            <div className="loader-container">
                <span className="loader"></span>
            </div>
        </div>
    );
}
