import './Banner.css'
function Banner(){
    return(
        <div className="hero-section">
            <div className='hero-text'>
                <h1>Groceries Delivered in 90 Minute</h1> 
                <p>Get your healthy foods & snacks delivered at your doorsteps all day everyday</p>
                <div className="search-container">
                    <input className='search-bar' type="text" name="" placeholder='Search your products from here' id=""/>
                    <button className='search-btn'><i className="fas fa-search"></i>Search</button>
                </div>
            </div>
            <div className='hero-image'>
            </div>
        </div>
    )
}
export default Banner;