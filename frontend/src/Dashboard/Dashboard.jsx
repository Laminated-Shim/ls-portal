import React, { useState } from 'react';

// leaving the navigation stupid like this. was learning states
import Navigation from './navigation.jsx'
import Stats from './Stats.jsx'
import Quotes from './Quotes/Quotes.jsx'



export default function Example() {
    const [activeTabName, setActiveTabName] = useState("Jobs");
    const handleIncrement = (activeTabName) => {
        setActiveTabName(activeTabName);        
      }
    return (
        <div>
            < Navigation onTabChange={handleIncrement} />     
            { activeTabName == "Jobs" &&
            <div>
                < Stats />
            </div>
            }
            { activeTabName == "Quotes" && 
            <div>
                < Quotes />
            </div>
            }   
        </div>
        
    )
}
    