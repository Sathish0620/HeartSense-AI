export default function RecommendationCard({ recommendation }) {
  if (!recommendation) return null;

  return (
    <div className="mt-8 rounded-2xl bg-white p-8 shadow-lg">

      <h2 className="text-2xl font-bold text-green-700">
        🥗 Recommendations
      </h2>

      <div className="mt-6">

        <p>
          <strong>Calories:</strong> {recommendation.calories}
        </p>

        <p className="mt-4 font-semibold">
          Exercise
        </p>

        <p>{recommendation.exercise}</p>

        <p className="mt-4 font-semibold">
          Water Intake
        </p>

        <p>{recommendation.water_intake}</p>

      </div>

    </div>
  );
}