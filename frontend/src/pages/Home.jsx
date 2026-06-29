import { useState } from "react";
import api from "../services/api";
import PatientForm from "../components/PatientForm";
import PredictionCard from "../components/PredictionCard";
import RecommendationCard from "../components/RecommendationCard";

export default function Home() {

  const [prediction, setPrediction] = useState(null);

  const handlePrediction = async (patientData) => {
    try {
        const response = await api.post("/predict", patientData);
        console.log("API Response:", response.data);
        setPrediction(response.data);

        } 
    catch (error) {
        console.error(error);

        alert("Prediction failed.");
    }
};


  return (
    <div className="min-h-screen bg-slate-100 p-10">

      <div className="max-w-5xl mx-auto">

        <h1 className="text-5xl font-extrabold text-red-600">
          ❤️ HeartSense AI
        </h1>

        <p className="mt-3 text-xl text-gray-600">
          AI-powered Heart Disease Prediction & Lifestyle Recommendation
        </p>

        <PatientForm onSubmit={handlePrediction}/>

        <PredictionCard
          result={prediction}/>

        <RecommendationCard
          recommendation={
            prediction?.recommendations
          }
        />

      </div>

    </div>
  );
}