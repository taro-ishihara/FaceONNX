﻿using System;
using System.Drawing;

namespace FaceONNX
{
    /// <summary>
    /// Defines face landmarks extractor interface.
    /// </summary>
    public interface IFaceLandmarksExtractor : IDisposable
    {
        #region Interface

        /// <summary>
        /// Returns face recognition results.
        /// </summary>
        /// <param name="image">Bitmap</param>
        /// <returns>Point</returns>
        Point[] Forward(Bitmap image);

        /// <summary>
        /// Returns face recognition results.
        /// </summary>
        /// <param name="image">Bitmap</param>
        /// <param name="rectangle">Rectangle</param>
        /// <returns>Point</returns>
        Point[] Forward(Bitmap image, Rectangle rectangle);

        /// <summary>
        /// Returns face recognition results.
        /// </summary>
        /// <param name="image">Image in BGR terms</param>
        /// <returns>Point</returns>
        Point[] Forward(float[][,] image);

        /// <summary>
        /// Returns face recognition results.
        /// </summary>
        /// <param name="image">Image in BGR terms</param>
        /// <param name="rectangle">Rectangle</param>
        /// <returns>Point</returns>
        Point[] Forward(float[][,] image, Rectangle rectangle);

        #endregion
    }
}
