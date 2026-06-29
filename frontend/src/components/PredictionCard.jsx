export default function PredictionCard({ result }) {
  if (!result) return null;

  return (
    <div className="mt-8 rounded-2xl bg-white p-8 shadow-lg">

      <h2 className="text-2xl font-bold text-red-600">
        ❤️ Prediction Result
      </h2>

      <div className="mt-6 space-y-3">

        <p>
          <strong>Prediction:</strong> {result.prediction}
        </p>

        <p>
          <strong>Risk Level:</strong> {result.risk_level}
        </p>

        <p>
          <strong>Confidence:</strong> {result.confidence}%
        </p>

      </div>

    </div>
  );
}