using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnMouseDown_Rotate : MonoBehaviour
{
    public float angle = 360;

    float rotateAngle = 0;

    private void OnMouseDown()
    {
        rotateAngle = angle;
    }

    private void OnMouseUp()
    {
        rotateAngle = 0;
    }

    private void FixedUpdate()
    {
        this.transform.Rotate(0, 0, rotateAngle / 50);
    }
}
